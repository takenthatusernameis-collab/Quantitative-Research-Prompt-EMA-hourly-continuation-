# EMA Hourly Continuation — RUNE/USDT P20_34

**Symbol:** RUNE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1140 |
| net_profit_factor | 0.3822 |
| net_win_rate | 0.4281 |
| gross_profit_factor | 0.8280 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -10.3060 |
| sortino_ratio | -4.9290 |
| max_drawdown | 0.9982 |
| cagr | -0.9184 |
| net_avg_win | 12.6549 |
| net_avg_loss | -24.7808 |
| avg_hold_time_bars | 2.5096 |
| exposure | 0.1300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
