# EMA Hourly Continuation — ARB/USDT P20_89

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.6312 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 1.0040 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -3.5991 |
| sortino_ratio | -1.3512 |
| max_drawdown | 0.8074 |
| cagr | -0.4777 |
| net_avg_win | 38.9900 |
| net_avg_loss | -60.9112 |
| avg_hold_time_bars | 11.7215 |
| exposure | 0.3788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
