# EMA Hourly Continuation — JTO/USDT P50_100

**Symbol:** JTO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.7227 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -1.9220 |
| sortino_ratio | -0.5259 |
| max_drawdown | 0.4994 |
| cagr | -0.2140 |
| net_avg_win | 67.5819 |
| net_avg_loss | -84.7886 |
| avg_hold_time_bars | 8.8913 |
| exposure | 0.1487 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
