# EMA Hourly Continuation — XMR/USDT P8_20

**Symbol:** XMR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.6324 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8898 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -2.4920 |
| sortino_ratio | -0.6206 |
| max_drawdown | 0.5102 |
| cagr | -0.2474 |
| net_avg_win | 61.8267 |
| net_avg_loss | -86.2211 |
| avg_hold_time_bars | 5.3828 |
| exposure | 0.0741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
