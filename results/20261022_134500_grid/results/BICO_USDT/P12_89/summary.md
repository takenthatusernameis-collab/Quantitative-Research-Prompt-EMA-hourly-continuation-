# EMA Hourly Continuation — BICO/USDT P12_89

**Symbol:** BICO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.7442 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 1.0081 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -2.5332 |
| sortino_ratio | -0.9231 |
| max_drawdown | 0.6840 |
| cagr | -0.3516 |
| net_avg_win | 59.3680 |
| net_avg_loss | -77.6210 |
| avg_hold_time_bars | 19.0395 |
| exposure | 0.5703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
