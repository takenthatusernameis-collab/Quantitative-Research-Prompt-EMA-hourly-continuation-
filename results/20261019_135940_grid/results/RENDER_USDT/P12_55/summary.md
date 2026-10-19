# EMA Hourly Continuation — RENDER/USDT P12_55

**Symbol:** RENDER/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 995 |
| net_profit_factor | 0.5563 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8506 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -6.4677 |
| sortino_ratio | -3.0748 |
| max_drawdown | 0.9647 |
| cagr | -0.7778 |
| net_avg_win | 26.0872 |
| net_avg_loss | -40.6490 |
| avg_hold_time_bars | 6.3236 |
| exposure | 0.3321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
