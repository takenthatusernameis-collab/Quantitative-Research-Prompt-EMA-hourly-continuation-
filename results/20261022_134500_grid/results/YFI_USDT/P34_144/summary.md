# EMA Hourly Continuation — YFI/USDT P34_144

**Symbol:** YFI/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.5969 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 1.0275 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -3.7791 |
| sortino_ratio | -1.2035 |
| max_drawdown | 0.7870 |
| cagr | -0.4422 |
| net_avg_win | 45.1057 |
| net_avg_loss | -71.6062 |
| avg_hold_time_bars | 17.9808 |
| exposure | 0.4231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
