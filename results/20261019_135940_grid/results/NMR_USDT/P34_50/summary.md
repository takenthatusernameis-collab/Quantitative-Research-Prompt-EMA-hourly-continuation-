# EMA Hourly Continuation — NMR/USDT P34_50

**Symbol:** NMR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 960 |
| net_profit_factor | 0.4148 |
| net_win_rate | 0.4042 |
| gross_profit_factor | 0.9211 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -10.0501 |
| sortino_ratio | -4.4175 |
| max_drawdown | 0.9965 |
| cagr | -0.8945 |
| net_avg_win | 18.2074 |
| net_avg_loss | -29.7713 |
| avg_hold_time_bars | 2.8802 |
| exposure | 0.1257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
