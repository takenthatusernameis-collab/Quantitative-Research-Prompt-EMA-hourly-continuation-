# EMA Hourly Continuation — TFUEL/USDT P34_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.4886 |
| net_win_rate | 0.3931 |
| gross_profit_factor | 0.7308 |
| gross_win_rate | 0.4032 |
| sharpe_ratio | -5.5003 |
| sortino_ratio | -1.7088 |
| max_drawdown | 0.8810 |
| cagr | -0.5645 |
| net_avg_win | 42.9714 |
| net_avg_loss | -56.9801 |
| avg_hold_time_bars | 20.3851 |
| exposure | 0.4575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
