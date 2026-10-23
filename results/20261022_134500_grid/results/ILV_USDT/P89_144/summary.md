# EMA Hourly Continuation — ILV/USDT P89_144

**Symbol:** ILV/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6448 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0555 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -2.9099 |
| sortino_ratio | -0.8861 |
| max_drawdown | 0.6506 |
| cagr | -0.3421 |
| net_avg_win | 50.6918 |
| net_avg_loss | -80.6921 |
| avg_hold_time_bars | 5.6087 |
| exposure | 0.1173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
