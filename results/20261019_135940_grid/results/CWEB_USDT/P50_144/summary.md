# EMA Hourly Continuation — CWEB/USDT P50_144

**Symbol:** CWEB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.5549 |
| net_win_rate | 0.4370 |
| gross_profit_factor | 0.8785 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -4.2451 |
| sortino_ratio | -1.1486 |
| max_drawdown | 0.7796 |
| cagr | -0.4354 |
| net_avg_win | 58.2765 |
| net_avg_loss | -81.5182 |
| avg_hold_time_bars | 19.9786 |
| exposure | 0.3387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
