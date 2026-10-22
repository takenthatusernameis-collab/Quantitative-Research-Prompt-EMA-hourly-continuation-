# EMA Hourly Continuation — LDO/USDT P8_89

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.6129 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8903 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -4.2339 |
| sortino_ratio | -1.4755 |
| max_drawdown | 0.8348 |
| cagr | -0.5118 |
| net_avg_win | 46.7024 |
| net_avg_loss | -63.6141 |
| avg_hold_time_bars | 24.2765 |
| exposure | 0.6864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
