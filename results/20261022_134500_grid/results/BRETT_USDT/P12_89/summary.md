# EMA Hourly Continuation — BRETT/USDT P12_89

**Symbol:** BRETT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.7087 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9421 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -3.2416 |
| sortino_ratio | -1.2318 |
| max_drawdown | 0.7492 |
| cagr | -0.4407 |
| net_avg_win | 56.1607 |
| net_avg_loss | -71.3226 |
| avg_hold_time_bars | 16.3728 |
| exposure | 0.5389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
