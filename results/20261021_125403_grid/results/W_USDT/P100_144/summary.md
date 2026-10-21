# EMA Hourly Continuation — W/USDT P100_144

**Symbol:** W/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 1.0337 |
| net_win_rate | 0.5768 |
| gross_profit_factor | 1.3477 |
| gross_win_rate | 0.5768 |
| sharpe_ratio | 0.2220 |
| sortino_ratio | 0.0504 |
| max_drawdown | 0.1372 |
| cagr | 0.0171 |
| net_avg_win | 96.0018 |
| net_avg_loss | -126.5589 |
| avg_hold_time_bars | 6.6224 |
| exposure | 0.0725 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
