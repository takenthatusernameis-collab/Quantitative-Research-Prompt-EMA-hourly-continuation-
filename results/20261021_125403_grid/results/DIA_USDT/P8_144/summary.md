# EMA Hourly Continuation — DIA/USDT P8_144

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.8075 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 0.9771 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -1.3062 |
| sortino_ratio | -0.3793 |
| max_drawdown | 0.4023 |
| cagr | -0.1618 |
| net_avg_win | 73.1658 |
| net_avg_loss | -89.3105 |
| avg_hold_time_bars | 38.1566 |
| exposure | 0.7165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
