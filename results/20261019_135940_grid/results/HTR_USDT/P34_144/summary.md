# EMA Hourly Continuation — HTR/USDT P34_144

**Symbol:** HTR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.5185 |
| net_win_rate | 0.4165 |
| gross_profit_factor | 0.7398 |
| gross_win_rate | 0.4229 |
| sharpe_ratio | -5.6294 |
| sortino_ratio | -1.9773 |
| max_drawdown | 0.9169 |
| cagr | -0.6182 |
| net_avg_win | 37.4435 |
| net_avg_loss | -51.5515 |
| avg_hold_time_bars | 12.9062 |
| exposure | 0.3690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
