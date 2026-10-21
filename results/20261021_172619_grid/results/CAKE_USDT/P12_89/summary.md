# EMA Hourly Continuation — CAKE/USDT P12_89

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.8277 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0670 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -1.3723 |
| sortino_ratio | -0.4350 |
| max_drawdown | 0.4664 |
| cagr | -0.1831 |
| net_avg_win | 76.2120 |
| net_avg_loss | -97.5180 |
| avg_hold_time_bars | 24.2295 |
| exposure | 0.5375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
