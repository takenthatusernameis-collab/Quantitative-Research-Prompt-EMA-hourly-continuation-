# EMA Hourly Continuation — XMR/USDT P12_20

**Symbol:** XMR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1776 |
| net_profit_factor | 0.0963 |
| net_win_rate | 0.3221 |
| gross_profit_factor | 0.3457 |
| gross_win_rate | 0.3502 |
| sharpe_ratio | -19.9825 |
| sortino_ratio | -12.3844 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 1.8640 |
| net_avg_loss | -9.1912 |
| avg_hold_time_bars | 1.7461 |
| exposure | 0.1410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
