# EMA Hourly Continuation — XAI/USDT P20_26

**Symbol:** XAI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.5364 |
| net_win_rate | 0.4302 |
| gross_profit_factor | 0.7287 |
| gross_win_rate | 0.4302 |
| sharpe_ratio | -3.0601 |
| sortino_ratio | -0.7082 |
| max_drawdown | 0.5657 |
| cagr | -0.2778 |
| net_avg_win | 56.6681 |
| net_avg_loss | -79.7568 |
| avg_hold_time_bars | 4.7132 |
| exposure | 0.0568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
