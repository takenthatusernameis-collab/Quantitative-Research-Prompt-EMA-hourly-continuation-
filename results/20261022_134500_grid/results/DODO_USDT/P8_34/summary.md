# EMA Hourly Continuation — DODO/USDT P8_34

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1402 |
| net_profit_factor | 0.5129 |
| net_win_rate | 0.4308 |
| gross_profit_factor | 0.8923 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -8.7603 |
| sortino_ratio | -4.5968 |
| max_drawdown | 0.9965 |
| cagr | -0.8936 |
| net_avg_win | 17.3711 |
| net_avg_loss | -25.6354 |
| avg_hold_time_bars | 5.9037 |
| exposure | 0.3745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
