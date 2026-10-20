# EMA Hourly Continuation — ERG/USDT P50_89

**Symbol:** ERG/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.2675 |
| net_win_rate | 0.3457 |
| gross_profit_factor | 0.5425 |
| gross_win_rate | 0.3680 |
| sharpe_ratio | -9.2863 |
| sortino_ratio | -3.4254 |
| max_drawdown | 0.9873 |
| cagr | -0.8230 |
| net_avg_win | 15.4704 |
| net_avg_loss | -30.5563 |
| avg_hold_time_bars | 5.6469 |
| exposure | 0.1730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
