# EMA Hourly Continuation — RENDER/USDT P12_89

**Symbol:** RENDER/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.6189 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8829 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -4.6202 |
| sortino_ratio | -1.8225 |
| max_drawdown | 0.8557 |
| cagr | -0.5843 |
| net_avg_win | 43.9785 |
| net_avg_loss | -60.4633 |
| avg_hold_time_bars | 14.4744 |
| exposure | 0.5218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
