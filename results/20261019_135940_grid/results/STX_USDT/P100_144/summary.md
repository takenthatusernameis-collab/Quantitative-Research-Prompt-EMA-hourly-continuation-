# EMA Hourly Continuation — STX/USDT P100_144

**Symbol:** STX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.4920 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.8841 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -4.4043 |
| sortino_ratio | -1.3217 |
| max_drawdown | 0.8183 |
| cagr | -0.4808 |
| net_avg_win | 35.7598 |
| net_avg_loss | -66.6026 |
| avg_hold_time_bars | 4.4869 |
| exposure | 0.0930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
