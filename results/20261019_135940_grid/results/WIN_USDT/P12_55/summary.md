# EMA Hourly Continuation — WIN/USDT P12_55

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 995 |
| net_profit_factor | 0.4011 |
| net_win_rate | 0.4221 |
| gross_profit_factor | 0.8715 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -8.9228 |
| sortino_ratio | -3.9586 |
| max_drawdown | 0.9940 |
| cagr | -0.8680 |
| net_avg_win | 15.8481 |
| net_avg_loss | -28.8597 |
| avg_hold_time_bars | 8.2030 |
| exposure | 0.3710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
