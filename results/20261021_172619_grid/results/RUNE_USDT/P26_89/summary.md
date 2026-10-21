# EMA Hourly Continuation — RUNE/USDT P26_89

**Symbol:** RUNE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.8228 |
| net_win_rate | 0.5222 |
| gross_profit_factor | 1.0711 |
| gross_win_rate | 0.5222 |
| sharpe_ratio | -1.1046 |
| sortino_ratio | -0.3113 |
| max_drawdown | 0.3628 |
| cagr | -0.1345 |
| net_avg_win | 70.6454 |
| net_avg_loss | -93.8313 |
| avg_hold_time_bars | 22.6710 |
| exposure | 0.3947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
