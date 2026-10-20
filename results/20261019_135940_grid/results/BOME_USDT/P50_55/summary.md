# EMA Hourly Continuation — BOME/USDT P50_55

**Symbol:** BOME/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 841 |
| net_profit_factor | 0.2242 |
| net_win_rate | 0.3615 |
| gross_profit_factor | 0.5716 |
| gross_win_rate | 0.3948 |
| sharpe_ratio | -11.6377 |
| sortino_ratio | -4.8689 |
| max_drawdown | 0.9987 |
| cagr | -0.9282 |
| net_avg_win | 9.4923 |
| net_avg_loss | -23.9706 |
| avg_hold_time_bars | 1.9049 |
| exposure | 0.0728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
