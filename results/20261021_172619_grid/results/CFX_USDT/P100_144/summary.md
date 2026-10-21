# EMA Hourly Continuation — CFX/USDT P100_144

**Symbol:** CFX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.7522 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0223 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.3590 |
| sortino_ratio | -0.2935 |
| max_drawdown | 0.3047 |
| cagr | -0.1259 |
| net_avg_win | 76.3866 |
| net_avg_loss | -103.3615 |
| avg_hold_time_bars | 6.5088 |
| exposure | 0.0669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
