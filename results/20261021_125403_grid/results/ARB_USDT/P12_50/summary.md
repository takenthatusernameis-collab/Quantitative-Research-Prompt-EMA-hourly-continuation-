# EMA Hourly Continuation — ARB/USDT P12_50

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.8150 |
| net_win_rate | 0.5153 |
| gross_profit_factor | 1.0402 |
| gross_win_rate | 0.5153 |
| sharpe_ratio | -1.3466 |
| sortino_ratio | -0.4571 |
| max_drawdown | 0.4618 |
| cagr | -0.1912 |
| net_avg_win | 63.4087 |
| net_avg_loss | -82.7025 |
| avg_hold_time_bars | 12.3591 |
| exposure | 0.3129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
