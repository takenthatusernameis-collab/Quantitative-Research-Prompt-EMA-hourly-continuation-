# EMA Hourly Continuation — MOVR/USDT P50_89

**Symbol:** MOVR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.4318 |
| net_win_rate | 0.4247 |
| gross_profit_factor | 0.7726 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -6.6208 |
| sortino_ratio | -2.4855 |
| max_drawdown | 0.9547 |
| cagr | -0.6981 |
| net_avg_win | 24.1586 |
| net_avg_loss | -41.3069 |
| avg_hold_time_bars | 4.7443 |
| exposure | 0.1518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
