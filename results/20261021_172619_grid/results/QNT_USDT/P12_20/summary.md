# EMA Hourly Continuation — QNT/USDT P12_20

**Symbol:** QNT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.7414 |
| net_win_rate | 0.5229 |
| gross_profit_factor | 1.0966 |
| gross_win_rate | 0.5229 |
| sharpe_ratio | -1.5323 |
| sortino_ratio | -0.3583 |
| max_drawdown | 0.3468 |
| cagr | -0.1508 |
| net_avg_win | 70.4889 |
| net_avg_loss | -104.1981 |
| avg_hold_time_bars | 4.9237 |
| exposure | 0.0586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
