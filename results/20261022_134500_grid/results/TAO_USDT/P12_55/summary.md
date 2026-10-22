# EMA Hourly Continuation — TAO/USDT P12_55

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1063 |
| net_profit_factor | 0.6462 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9511 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -5.2471 |
| sortino_ratio | -2.4215 |
| max_drawdown | 0.9463 |
| cagr | -0.6825 |
| net_avg_win | 34.0757 |
| net_avg_loss | -47.9023 |
| avg_hold_time_bars | 7.1082 |
| exposure | 0.3435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
