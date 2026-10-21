# EMA Hourly Continuation — XCN/USDT P12_89

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.7139 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.8898 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -2.4469 |
| sortino_ratio | -0.7915 |
| max_drawdown | 0.6130 |
| cagr | -0.3063 |
| net_avg_win | 61.4436 |
| net_avg_loss | -76.9266 |
| avg_hold_time_bars | 19.6499 |
| exposure | 0.4618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
