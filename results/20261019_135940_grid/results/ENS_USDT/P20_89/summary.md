# EMA Hourly Continuation — ENS/USDT P20_89

**Symbol:** ENS/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.6314 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9583 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -4.0050 |
| sortino_ratio | -1.5061 |
| max_drawdown | 0.8543 |
| cagr | -0.5118 |
| net_avg_win | 41.9333 |
| net_avg_loss | -61.2082 |
| avg_hold_time_bars | 12.8678 |
| exposure | 0.4159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
