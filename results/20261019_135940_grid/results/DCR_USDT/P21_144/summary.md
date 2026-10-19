# EMA Hourly Continuation — DCR/USDT P21_144

**Symbol:** DCR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.6195 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9204 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -3.1534 |
| sortino_ratio | -1.0850 |
| max_drawdown | 0.7419 |
| cagr | -0.4005 |
| net_avg_win | 40.5667 |
| net_avg_loss | -62.6799 |
| avg_hold_time_bars | 18.2269 |
| exposure | 0.4907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
