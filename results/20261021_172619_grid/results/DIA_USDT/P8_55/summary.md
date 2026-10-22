# EMA Hourly Continuation — DIA/USDT P8_55

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.7270 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9343 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -2.7444 |
| sortino_ratio | -1.0566 |
| max_drawdown | 0.7362 |
| cagr | -0.3853 |
| net_avg_win | 53.1790 |
| net_avg_loss | -68.6880 |
| avg_hold_time_bars | 13.3529 |
| exposure | 0.4417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
