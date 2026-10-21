# EMA Hourly Continuation — APT/USDT P20_200

**Symbol:** APT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.9322 |
| net_win_rate | 0.5246 |
| gross_profit_factor | 1.0887 |
| gross_win_rate | 0.5246 |
| sharpe_ratio | -0.3008 |
| sortino_ratio | -0.0676 |
| max_drawdown | 0.1923 |
| cagr | -0.0339 |
| net_avg_win | 89.2032 |
| net_avg_loss | -105.5853 |
| avg_hold_time_bars | 60.8156 |
| exposure | 0.6745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
