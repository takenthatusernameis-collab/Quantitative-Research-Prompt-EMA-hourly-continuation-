# EMA Hourly Continuation — DIA/USDT P20_26

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1164 |
| net_profit_factor | 0.2176 |
| net_win_rate | 0.4038 |
| gross_profit_factor | 0.7137 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -12.0165 |
| sortino_ratio | -5.8577 |
| max_drawdown | 0.9995 |
| cagr | -0.9513 |
| net_avg_win | 5.9159 |
| net_avg_loss | -18.4087 |
| avg_hold_time_bars | 2.3325 |
| exposure | 0.1229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
