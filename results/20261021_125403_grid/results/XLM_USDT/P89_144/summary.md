# EMA Hourly Continuation — XLM/USDT P89_144

**Symbol:** XLM/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.6250 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9277 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -2.1753 |
| sortino_ratio | -0.4820 |
| max_drawdown | 0.4295 |
| cagr | -0.1975 |
| net_avg_win | 61.5157 |
| net_avg_loss | -92.0240 |
| avg_hold_time_bars | 8.4580 |
| exposure | 0.0915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
