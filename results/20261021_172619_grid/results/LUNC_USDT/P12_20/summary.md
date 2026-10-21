# EMA Hourly Continuation — LUNC/USDT P12_20

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.5843 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.8485 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -2.5254 |
| sortino_ratio | -0.5447 |
| max_drawdown | 0.4735 |
| cagr | -0.2214 |
| net_avg_win | 63.0621 |
| net_avg_loss | -91.2496 |
| avg_hold_time_bars | 4.3965 |
| exposure | 0.0454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
