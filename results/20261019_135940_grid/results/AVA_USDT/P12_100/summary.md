# EMA Hourly Continuation — AVA/USDT P12_100

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.5504 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.8537 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -4.3405 |
| sortino_ratio | -1.6066 |
| max_drawdown | 0.8689 |
| cagr | -0.5456 |
| net_avg_win | 31.6876 |
| net_avg_loss | -51.6779 |
| avg_hold_time_bars | 16.2017 |
| exposure | 0.5185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
