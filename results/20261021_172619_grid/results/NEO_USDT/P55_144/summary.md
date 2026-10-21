# EMA Hourly Continuation — NEO/USDT P55_144

**Symbol:** NEO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.6380 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8534 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -2.4535 |
| sortino_ratio | -0.6615 |
| max_drawdown | 0.5416 |
| cagr | -0.2615 |
| net_avg_win | 55.8977 |
| net_avg_loss | -77.8823 |
| avg_hold_time_bars | 13.6863 |
| exposure | 0.2221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
