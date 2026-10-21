# EMA Hourly Continuation — ARB/USDT P20_21

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 115 |
| net_profit_factor | 0.4994 |
| net_win_rate | 0.4087 |
| gross_profit_factor | 0.6856 |
| gross_win_rate | 0.4087 |
| sharpe_ratio | -2.2607 |
| sortino_ratio | -0.3447 |
| max_drawdown | 0.3464 |
| cagr | -0.1471 |
| net_avg_win | 69.9322 |
| net_avg_loss | -96.7776 |
| avg_hold_time_bars | 4.9304 |
| exposure | 0.0258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
