# EMA Hourly Continuation — TFUEL/USDT P50_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.5435 |
| net_win_rate | 0.4093 |
| gross_profit_factor | 0.7155 |
| gross_win_rate | 0.4093 |
| sharpe_ratio | -4.1915 |
| sortino_ratio | -1.2274 |
| max_drawdown | 0.7687 |
| cagr | -0.4333 |
| net_avg_win | 51.5082 |
| net_avg_loss | -65.6633 |
| avg_hold_time_bars | 12.9326 |
| exposure | 0.2516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
