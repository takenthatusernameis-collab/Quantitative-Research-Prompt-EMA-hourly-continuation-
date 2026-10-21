# EMA Hourly Continuation — ZEN/USDT P8_144

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 1.0437 |
| net_win_rate | 0.5529 |
| gross_profit_factor | 1.2296 |
| gross_win_rate | 0.5529 |
| sharpe_ratio | 0.2963 |
| sortino_ratio | 0.0783 |
| max_drawdown | 0.1141 |
| cagr | 0.0278 |
| net_avg_win | 93.0177 |
| net_avg_loss | -110.2006 |
| avg_hold_time_bars | 51.6888 |
| exposure | 0.7777 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
