# EMA Hourly Continuation — LDO/USDT P50_144

**Symbol:** LDO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6268 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8590 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -3.2865 |
| sortino_ratio | -1.0210 |
| max_drawdown | 0.7114 |
| cagr | -0.3775 |
| net_avg_win | 52.4187 |
| net_avg_loss | -72.8468 |
| avg_hold_time_bars | 13.9582 |
| exposure | 0.3039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
