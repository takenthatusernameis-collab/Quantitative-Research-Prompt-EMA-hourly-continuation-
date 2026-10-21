# EMA Hourly Continuation — TWT/USDT P12_55

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.7622 |
| net_win_rate | 0.5191 |
| gross_profit_factor | 1.0621 |
| gross_win_rate | 0.5206 |
| sharpe_ratio | -2.0270 |
| sortino_ratio | -0.7612 |
| max_drawdown | 0.6115 |
| cagr | -0.2948 |
| net_avg_win | 53.0338 |
| net_avg_loss | -75.1130 |
| avg_hold_time_bars | 11.7647 |
| exposure | 0.3636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
