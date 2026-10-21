# EMA Hourly Continuation — CELO/USDT P12_34

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.7041 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9671 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -2.8884 |
| sortino_ratio | -1.0652 |
| max_drawdown | 0.7085 |
| cagr | -0.3866 |
| net_avg_win | 51.4094 |
| net_avg_loss | -70.8510 |
| avg_hold_time_bars | 7.3228 |
| exposure | 0.2207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
