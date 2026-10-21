# EMA Hourly Continuation — LSK/USDT P12_26

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.6402 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 1.0090 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -4.2681 |
| sortino_ratio | -1.5522 |
| max_drawdown | 0.8402 |
| cagr | -0.5103 |
| net_avg_win | 48.7941 |
| net_avg_loss | -68.5473 |
| avg_hold_time_bars | 6.0872 |
| exposure | 0.1776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
