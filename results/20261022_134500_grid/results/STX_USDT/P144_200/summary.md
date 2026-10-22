# EMA Hourly Continuation — STX/USDT P144_200

**Symbol:** STX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.5625 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -3.4026 |
| sortino_ratio | -0.8932 |
| max_drawdown | 0.6720 |
| cagr | -0.3568 |
| net_avg_win | 49.9029 |
| net_avg_loss | -86.7111 |
| avg_hold_time_bars | 4.9486 |
| exposure | 0.0784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
