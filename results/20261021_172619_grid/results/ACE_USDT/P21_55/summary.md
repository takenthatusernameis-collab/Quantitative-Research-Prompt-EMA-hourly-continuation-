# EMA Hourly Continuation — ACE/USDT P21_55

**Symbol:** ACE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.7504 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0109 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -1.8421 |
| sortino_ratio | -0.6057 |
| max_drawdown | 0.5457 |
| cagr | -0.2425 |
| net_avg_win | 56.0966 |
| net_avg_loss | -78.5321 |
| avg_hold_time_bars | 9.4099 |
| exposure | 0.2244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
