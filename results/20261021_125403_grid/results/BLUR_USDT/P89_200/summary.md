# EMA Hourly Continuation — BLUR/USDT P89_200

**Symbol:** BLUR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.8123 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0265 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -1.0780 |
| sortino_ratio | -0.2544 |
| max_drawdown | 0.2866 |
| cagr | -0.1118 |
| net_avg_win | 81.0679 |
| net_avg_loss | -102.7769 |
| avg_hold_time_bars | 18.5882 |
| exposure | 0.2288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
