# EMA Hourly Continuation — DUSK/USDT P12_100

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.6255 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8575 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -4.0681 |
| sortino_ratio | -1.4994 |
| max_drawdown | 0.8372 |
| cagr | -0.5067 |
| net_avg_win | 45.1747 |
| net_avg_loss | -58.8154 |
| avg_hold_time_bars | 18.2763 |
| exposure | 0.5682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
