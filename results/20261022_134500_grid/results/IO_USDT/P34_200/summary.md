# EMA Hourly Continuation — IO/USDT P34_200

**Symbol:** IO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.7274 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9551 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -2.0819 |
| sortino_ratio | -0.5853 |
| max_drawdown | 0.5074 |
| cagr | -0.2467 |
| net_avg_win | 70.2847 |
| net_avg_loss | -92.6155 |
| avg_hold_time_bars | 26.1111 |
| exposure | 0.4778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
