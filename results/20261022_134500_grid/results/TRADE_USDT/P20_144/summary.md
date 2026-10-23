# EMA Hourly Continuation — TRADE/USDT P20_144

**Symbol:** TRADE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.7026 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8775 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -2.1640 |
| sortino_ratio | -0.6033 |
| max_drawdown | 0.5260 |
| cagr | -0.2455 |
| net_avg_win | 65.8206 |
| net_avg_loss | -82.7682 |
| avg_hold_time_bars | 29.3170 |
| exposure | 0.5170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
