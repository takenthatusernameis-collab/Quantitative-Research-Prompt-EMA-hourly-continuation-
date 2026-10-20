# EMA Hourly Continuation — T/USDT P50_89

**Symbol:** T/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.4470 |
| net_win_rate | 0.4271 |
| gross_profit_factor | 0.8069 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -6.3690 |
| sortino_ratio | -2.1480 |
| max_drawdown | 0.9356 |
| cagr | -0.6573 |
| net_avg_win | 30.6521 |
| net_avg_loss | -51.1186 |
| avg_hold_time_bars | 7.3906 |
| exposure | 0.1926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
